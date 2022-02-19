import {Component, OnDestroy, OnInit} from '@angular/core';
// import {prod, products} from '../shared/mockData';
import {ProductService} from '../../services/product.service';
import {ActivatedRoute} from '@angular/router';
import {Subscription} from "rxjs";
import { ProductInfo } from 'src/app/models/productInfo';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit, OnDestroy {


  title: string;
  private paramSub: Subscription;
  private querySub: Subscription;
  products: ProductInfo[];

  constructor(private productService: ProductService,
              private route: ActivatedRoute) {

  }


  ngOnInit() {
    this.querySub = this.route.queryParams.subscribe(() => {
      this.update();
    });
    this.paramSub = this.route.params.subscribe(() => {
      this.update();
    });

  }

  ngOnDestroy(): void {
    this.querySub.unsubscribe();
    this.paramSub.unsubscribe();
  }

  update() {
    if (this.route.snapshot.queryParamMap.get('page')) {
      const currentPage = +this.route.snapshot.queryParamMap.get('page');
      const size = +this.route.snapshot.queryParamMap.get('size');
      this.getProds(currentPage, size);
    } else {
      this.getProds();
    }
  }
  getProds(page: number = 1, size: number = 3) {
    if (this.route.snapshot.url.length == 1) {
      this.productService.getAllInPage()
        .subscribe(prod => {
          this.products = prod;
          this.title = 'Get Whatever You Want!';
          console.log(this.products);
        });
    } else { //  /category/:id
      const type = this.route.snapshot.url[1].path;
      this.productService.getCategoryInPage(+type)
        .subscribe(products => {
          console.log(products);
          // this.title = categoryPage.category;
          //TODO: zalatwic to
          this.products = products;
        });
    }
    
  }


}
