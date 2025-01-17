import { Component, ElementRef, NgZone, OnInit } from '@angular/core';
import Scrollbar from 'smooth-scrollbar';

export const scrollbarOptions = {
  speed: 1,
  damping: 0.2,
  thumbMinSize: 20,
  syncCallbacks: true,
  renderByPixels: true,
  alwaysShowTracks: false,
  continuousScrolling: true,
  overscrollEffect: 'bounce',
  overscrollDamping: 0.2
};

@Component({
  selector: 'vr-scrollbar',
  templateUrl: './scrollbar.component.html',
  styleUrls: ['./scrollbar.component.scss']
})
export class ScrollbarComponent implements OnInit {

  scrollbarRef: Scrollbar;
  element: ElementRef;

  constructor(
    private _element: ElementRef,
    private zone: NgZone
  ) { }

  ngOnInit() {
    this.element = this._element;

    const options = scrollbarOptions;

    this.zone.runOutsideAngular(() => {
      this.scrollbarRef = Scrollbar.init(this.element.nativeElement, options);
    });
  }
}
