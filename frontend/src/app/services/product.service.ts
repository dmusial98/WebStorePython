import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {catchError} from 'rxjs/operators';
import {ProductInfo} from '../models/productInfo';
import {apiUrl} from '../../environments/environment';

@Injectable({
    providedIn: 'root'
})
export class ProductService {

    private productUrl = `${apiUrl}/products/`;
    private categoryUrl = `${apiUrl}/category`;

    constructor(private http: HttpClient) {
    }

    getAllInPage(): Observable<ProductInfo[]> {
        // const url = `${this.productUrl}?page=${page}&size=${size}`;
        const url = `${this.productUrl}`;
        return this.http.get<ProductInfo[]>(url)
            .pipe(
                // tap(_ => console.log(_)),
            )
    }

    getCategoryInPage(categoryType: number): Observable<any> {
        const url = `${this.productUrl}?categoryType=${categoryType}`;
        return this.http.get(url).pipe(
            // tap(data => console.log(data))
        );
    }

    getDetail(id: String): Observable<any> {
        const url = `${this.productUrl}${id}/`;
        return this.http.get<any>(url);
        // .pipe(
        //     catchError(_ => {
        //         console.log("Get Detail Failed");
        //         return of(new ProductInfo());
        //     })
        // );
    }

    update(productInfo: ProductInfo): Observable<ProductInfo> {
        
        const url = `${this.productUrl}${productInfo.productId}/`;
        return this.http.put<ProductInfo>(url, productInfo);
    }

    create(productInfo: ProductInfo): Observable<ProductInfo> {
        const url = `${apiUrl}/seller/product/new`;
        return this.http.post<ProductInfo>(url, productInfo);
    }


    delelte(productInfo: ProductInfo): Observable<any> {
        const url = `${apiUrl}/seller/product/${productInfo.productId}/delete`;
        return this.http.delete(url);
    }


    /**
     * Handle Http operation that failed.
     * Let the app continue.
     * @param operation - name of the operation that failed
     * @param result - optional value to return as the observable result
     */
    private handleError<T>(operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {

            console.error(error); // log to console instead

            // Let the app keep running by returning an empty result.
            return of(result as T);
        };
    }
}
