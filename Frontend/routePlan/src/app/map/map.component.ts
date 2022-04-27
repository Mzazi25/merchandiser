import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  apiLoaded: Observable<boolean>;
  constructor(httpClient: HttpClient) {
    this.apiLoaded = httpClient.jsonp('https://maps.googleapis.com/maps/api/js?key=AIzaSyDAA3xuCSY0YXlP9TBanYuRgnNst2SE1vA', 'callback')
    .pipe(
      map(() => true),
      catchError(() => of(false)),
    );
   }

  ngOnInit(): void {
  }

}