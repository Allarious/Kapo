import React from 'react';

import classes from './error/error.css';

const Error = () => {
    return(
        <div className={classes.container}>
        <div className={classes["text-wrapper"]}>
            <div className={classes.title} data-content="404">
                404
            </div>

            <div className={classes.subtitle} data-content="Oops, the page you're looking for doesn't exist">
                Oops, the page you're looking for doesn't exist.
            </div>

            <div className={classes.buttons}>
                <a className={classes.button} href="">Go to homepage</a>
            </div>
        </div>
        </div>
    );
};

export default Error;