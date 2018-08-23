import React from 'react';

import classes from '../footer.css';
const Wrapper = (props) => {

    let buttons = <div></div>;

    if (props.makeButton)
    {
        buttons = props.buttons.map((btn) => {
           return (<button key={btn.id} className={classes["wrapper-body-button"]}>{btn.txt}</button>);
        });
    }

    return (
        <div>
            <div className={classes["wrapper-header"]}>{props.head}</div>
            <div className={classes["wrapper-body"]}>
                {props.bod}
                {buttons}
                </div>
        </div>
    );
};

export default Wrapper;