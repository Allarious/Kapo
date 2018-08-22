import React from 'react';

import classes from './homepage/homepage.css';
import FirstGlance from './homepage/firstglance';
import Services from './homepage/services';
import OurTeam from './homepage/ourteam';

const Homepage = () => {
    return (
        <div>
            <FirstGlance/>
            <Services/>
            <OurTeam/>
        </div>
    );
};

export default Homepage;