import React from 'react';

import classes from './firstglance.css';

const FirstGlance = () => {
  return(
      <div className={classes.container}>
          <div className={classes.head}>
              <div className={classes["site-name"]}>Kapo</div>
              <div className={classes.motto}>Everything Will Be A Lot Easier From Now On!</div>
          </div>
          <div className={classes["item-container"]}>
              <div className={classes.item}>
                  <div className={classes.pic}></div>
                  <div className={classes.line}></div>
              </div>
              <div className={classes.item}>
                  <div className={classes.pic}></div>
                  <div className={classes.line}></div>
              </div>
              <div className={classes["item-animate"]}>
              <div className={classes.item}>
                  <div className={classes.pic}></div>
                  <div className={classes.line}></div>
              </div>
              </div>
          </div>
          <div className={classes.card}>
              <div className={classes.visa}>
                  <svg width="54px" height="18px" viewBox="0 0 54 18" version="1.1">
                      <g id="Page-1" stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
                          <g id="Desktop-HD" transform="translate(-880.000000, -450.000000)" fillRule="nonzero"
                             fill="#464F56">
                              <g id="Group-12" transform="translate(857.000000, 425.000000)">
                                  <g id="card">
                                      <g id="Visa_Inc._logo" transform="translate(23.276576, 25.726742)">
                                          <polygon id="polygon9"
                                                   points="23.0863929 16.9935312 18.7706301 16.9935312 21.4700174 0.302548034 25.7855442 0.302548034"></polygon>
                                          <path
                                              d="M38.7314166,0.710594948 C37.8801586,0.372876536 36.5299929,-6.12702237e-06 34.860517,-6.12702237e-06 C30.5985626,-6.12702237e-06 27.5973291,2.2726901 27.578921,5.52196131 C27.5435207,7.91926643 29.7277163,9.25078794 31.36132,10.0501256 C33.0310319,10.8669275 33.598616,11.4000553 33.598616,12.1281205 C33.5816239,13.2462965 32.2493944,13.7617242 31.0068455,13.7617242 C29.2837972,13.7617242 28.3605586,13.4959863 26.9575286,12.8738858 L26.3892365,12.6072039 L25.7853082,16.3539667 C26.7975194,16.815114 28.6624047,17.2243409 30.5985626,17.242277 C35.1269629,17.242277 38.075096,15.004745 38.1100242,11.5421283 C38.1272523,9.64207873 36.9739121,8.18618433 34.4873983,6.99649984 C32.9779316,6.23279838 32.053513,5.71784271 32.053513,4.93644113 C32.0712131,4.22607605 32.8353865,3.49848286 34.5393187,3.49848286 C35.9423487,3.4628466 36.9732041,3.80009301 37.7541337,4.13757542 L38.1444805,4.31481269 L38.7314166,0.710594948 L38.7314166,0.710594948 L38.7314166,0.710594948 Z"
                                              id="path11"></path>
                                          <path
                                              d="M44.4674376,11.080509 C44.8228561,10.1216342 46.1904859,6.41050765 46.1904859,6.41050765 C46.1725498,6.44614391 46.5451964,5.43393268 46.758306,4.81254024 L47.0599161,6.25073451 C47.0599161,6.25073451 47.87719,10.246007 48.0546632,11.080509 C47.3801704,11.080509 45.3198757,11.080509 44.4674376,11.080509 L44.4674376,11.080509 Z M49.7947037,0.302548034 L46.4564598,0.302548034 C45.4270205,0.302548034 44.6449109,0.604158188 44.2007557,1.68740592 L37.7902419,16.9932952 L42.3186423,16.9932952 C42.3186423,16.9932952 43.0641716,14.9332365 43.2244167,14.4895533 C43.7212003,14.4895533 48.1264077,14.4895533 48.7655003,14.4895533 C48.8894012,15.0755455 49.280456,16.9932952 49.280456,16.9932952 L53.2764365,16.9932952 L49.7947037,0.302548034 L49.7947037,0.302548034 L49.7947037,0.302548034 Z"
                                              id="path13"></path>
                                          <path
                                              d="M15.1659404,0.302548034 L10.9393862,11.6842013 L10.4775309,9.37586883 C9.69612929,6.71235381 7.24548779,3.81850114 4.51070026,2.37959887 L8.38207191,16.9758311 L12.9458725,16.9758311 L19.7295049,0.302548034 L15.1659404,0.302548034 L15.1659404,0.302548034 L15.1659404,0.302548034 Z"
                                              id="path15"></path>
                                          <path
                                              d="M7.01467814,0.302548034 L0.0710365562,0.302548034 L4.89161542e-08,0.639794442 C5.41647473,2.02488833 9.00370035,5.36360418 10.4775309,9.37657684 L8.96806409,1.70557805 C8.71955432,0.63955844 7.95585287,0.337712285 7.01467814,0.302548034 L7.01467814,0.302548034 Z"
                                              id="path17"></path>
                                      </g>
                                  </g>
                              </g>
                          </g>
                      </g>
                  </svg>
                  <div className={classes.num}>
                      1321 5328 1249 1249
                  </div>
                  <div className={classes.name}>
                      Burak Aslan
                  </div>
              </div>
          </div>
      </div>

  );
};

export default FirstGlance;