import React from 'react';

import classes from './aboutus/aboutus.css';

const AboutUs = () => {
    return(<div className={classes.container}>
        <div className={classes.header}>A LITTLE SOMETHING ABOUT US</div>
        <div className={classes.text}>CMT panels have been in the industry for over 30 years. Our aim is to bring your project vision to reality. With unrivaled experience in the sandwich panel and cool room industry, you can rest assured knowing that our team of accredited builders, installers and project managers will assist you with your project from start to finish no matter how big or small. CMT panels is leading the industry by staying abreast with technology using the latest in panel installing techniques, we have been trusted to play a large part in installing some of Australasia's biggest projects. Using only the best available materials on the market and a focus on quality, you can be at ease knowing that you are in good hands at CMT panels.</div>
        <div className={classes.timeline}>
            <section className={classes.timeline}>
                <div className={classes.wrapper}>
                    <div className={classes.timeline__item}>
                    <div className={classes.timeline__item__0}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>1987 Aug. 20</h2>
                            <p className={classes.timeline__item__content__description}>Began learning in the panel industry by
                                working with some of Australia biggest companies including pacesetter, portacom, Ausco
                                and James Hardies.</p>
                        </div>
                    </div></div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>1998 Sept. 5</h2>
                            <p className={classes.timeline__item__content__description}>Started installing various cool rooms
                                and freezers around the country.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>1995 Mar. 5</h2>
                            <p className={classes.timeline__item__content__description}>As well as contracting for ALL the major
                                sandwich panel building companies, we began to take a
                                keen interest in cool room construction.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2000 July 9</h2>
                            <p className={classes.timeline__item__content__description}>On top of cool room, chassis and
                                portable building fabrication , we begin a partnership with one of Australia's largest
                                manufacturer of switch rooms, temperature controlled shelters and specific designed
                                transportable rooms furthering our knowledge in this field. To date close to 9000
                                sandwich panel buildings have been manufactured by CMT panels with our partner.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2003 Nov. 12</h2>
                            <p className={classes.timeline__item__content__description}>We become what we are now known as CMT
                                Panels.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2009 Aug. 25</h2>
                            <p className={classes.timeline__item__content__description}>We begin our part in the Gorgon project,
                                Barrow Island WA. This was at the time one of the largest construction jobs hapenning in
                                the world.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2011 Aug. 03</h2>
                            <p className={classes.timeline__item__content__description}>We move premises to Thomaston in
                                Victoria to help accommodate larger projects and expand.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2012 Jan. 24</h2>
                            <p className={classes.timeline__item__content__description}>We begin our part on the Wheatstone
                                project, Onslow WA, also one of the largest construction jobs in the world.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2014 Apr. 28</h2>
                            <p className={classes.timeline__item__content__description}>Our crew of guys help with the south
                                Melbourne market relocation.</p>
                        </div>
                    </div>
                    <div className={classes.timeline__item}>
                        <div className={classes.timeline__item__station}></div>
                        <div className={classes.timeline__item__content}>
                            <h2 className={classes.timeline__item__content__date}>2017 +</h2>
                            <p className={classes.timeline__item__content__description}>Our company continues to grow and make
                                marks in the construction industry.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>);
}

export default AboutUs;