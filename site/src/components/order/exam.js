import React from 'react';

import classes from './exam.css';

const Exam = (props) => {

    let style = {
        backgroundImage: 'url(' + props.image + ')',
    };

    return(
        <div className={classes.container} onClick={() => props.clicked('Fill Exam')}>
            <div className={classes.header}>{props.name}</div>
            <div className={classes.image} style={style}/>
        </div>
    );

};

export default Exam;