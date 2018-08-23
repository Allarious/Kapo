import React from 'react';

import classes from './convert/convert.css';
import ConvertType from './convert/converttype';

const Convert = (props) => {
    const changes = [
        {
            money: 'Rial',
            remain: '153000000R',
            id:'c1',
        },
        {
            money:'Dollar',
            remain: '27$',
            id:'c2',
        },
        {
            money:'Euro',
            remain: '13E',
            id: 'c3',
        },
    ];
    return(
      <div className={classes.container}>
          {changes.map((event, index) => {
              return (
                <ConvertType type={event.money}
                             index={index}
                             remain={event.remain}
                             key={event.id}/>
              );
          })}
      </div>
    );
};

export default Convert;

