import React from 'react';

import classes from './homepage/homepage.css';
import FirstGlance from './homepage/firstglance';
import Services from './homepage/services';

const Homepage = () => {
    return (
        <div>
            <FirstGlance/>
            <Services/>
        </div>
    );
};

export default Homepage;