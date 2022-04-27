import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { GoogleMapsModule } from '@angular/google-maps';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MapComponent } from './map/map.component';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClientJsonpModule } from '@angular/common/http';
@NgModule({
  declarations: [
    AppComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    GoogleMapsModule,
    CommonModule,
    HttpClientModule,
    HttpClientJsonpModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
