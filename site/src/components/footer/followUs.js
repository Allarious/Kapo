import React from 'react';

import Wrapper from './components/wrapper';

const FollowUs = () => {

    let buttons = [
        {id: 'b1', txt:'Telegram'},
        {id:'b2', txt:'Instagram'},
    ];

    return <Wrapper head={'Follow Us'} makeButton={true} buttons={buttons}/>;
};

export default FollowUs;