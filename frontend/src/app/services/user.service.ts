import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {apiUrl} from '../../environments/environment';
import {BehaviorSubject, Observable, of, Subject} from 'rxjs';
import {catchError, tap} from 'rxjs/operators';
import {JwtResponse} from '../response/JwtResponse';
import {CookieService} from 'ngx-cookie-service';
import {User} from "../models/User";
import { JwtHelperService } from "@auth0/angular-jwt";

@Injectable({
    providedIn: 'root'
})
export class UserService {

    private currentUserSubject: BehaviorSubject<JwtResponse>;
    public currentUser: Observable<JwtResponse>;
    public nameTerms = new Subject<string>();
    public name$ = this.nameTerms.asObservable();
    constructor(private http: HttpClient,
                private cookieService: CookieService,
                private jwtHelper: JwtHelperService) {
        const memo = localStorage.getItem('currentUser');
        this.currentUserSubject = new BehaviorSubject<JwtResponse>(JSON.parse(memo));
        this.currentUser = this.currentUserSubject.asObservable();
        cookieService.set('currentUser', memo);
    }

    get currentUserValue() {
        return this.currentUserSubject.value;
    }


    login(loginForm): Observable<JwtResponse> {
        const url = `http://localhost:8000/api/token/`;
        return this.http.post<JwtResponse>(url, loginForm).pipe(
            tap(data => {
                console.log(data);
                var user = new User();

                if (data && data.access) {
                    console.log(data, data.access)
                    
                    const token = data.access;
                    if (token && !this.jwtHelper.isTokenExpired(token)) {
                        var decodedToken = this.jwtHelper.decodeToken(token);
  
                        user.email = decodedToken['email'];
                        user.name = decodedToken['name'];
                        user.phone = decodedToken['phone'];
                        user.address = decodedToken['address'];
                        user.active = decodedToken['active'];
                        user.role = decodedToken['role'];
                    
                        this.cookieService.set('currentUser', JSON.stringify(user));
                        localStorage.setItem('currentUser', JSON.stringify(user));
                        this.nameTerms.next(user.name);

                        var jwtResponse = new JwtResponse();
                        jwtResponse.token = decodedToken['access'];
                        jwtResponse.access = decodedToken['access'];
                        jwtResponse.name = decodedToken['name'];
                        jwtResponse.role = decodedToken['role'];


                        this.currentUserSubject.next(jwtResponse);
                        return user;
                    }
                }
            }),
            catchError(this.handleError('Login Failed', null))
        );
    }

    logout() {
        this.currentUserSubject.next(null);
        localStorage.removeItem('currentUser');
        this.cookieService.delete('currentUser');
    }

    signUp(user: User): Observable<User> {
        const url = `${apiUrl}/users/create/`;
        return this.http.post<User>(url, user);
    }

    update(user: User): Observable<any> {
        const url = `${apiUrl}/users/byName/${user.name}/`;
        return this.http.put<User>(url, user);    }

    get(name: string): Observable<any> {
        const url = `${apiUrl}/users/byName/${name}/`;
        return this.http.get<any>(url);
    }

    /**
     * Handle Http operation that failed.
     * Let the app continue.
     * @param operation - name of the operation that failed
     * @param result - optional value to return as the observable result
     */
    private handleError<T>(operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {

            console.log(error); // log to console instead

            // Let the app keep running by returning an empty result.
            return of(result as T);
        };
    }
}
