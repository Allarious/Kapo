import React, {Component} from 'react';

import classes from './order/order.css';
import Exam from './order/exam';
import Inp from './inputs/input';
import Button from './buttons/authbutton';

class Order extends Component {

    exams = [
        {
            name: 'Tofel',
            image: "https://yt3.ggpht.com/-Qj3MuJufOYo/AAAAAAAAAAI/AAAAAAAAAAA/YxqFm1RvezU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
            id: 'e1',
        }, {
            name: 'IELTS',
            image: "https://takeielts.britishcouncil.org/sites/default/files/2018-02/IELTS_app_icon.png",
            id: 'e2',
        }, {
            name: 'International Exams',
            image: "https://images.careers360.mobi/sites/default/files/2016/10/04/GRE_Test-2016.jpg",
            id: 'e3',
        }, {
            name: 'Cryptocurrency',
            image: "https://pbs.twimg.com/profile_images/421692600446619648/dWAbC2wg.jpeg",
            id: 'e4',
        },
    ];

    render() {
        return (
            <div className={classes.container}>
                {this.exams.map((event) => {
                    return (

                        <Exam key={event.id} name={event.name} image={event.image} clicked={this.props.clicked}/>

                    );
                })}
                <div className={classes.add}>
                    <div className={classes.circle}>
                        <div className={classes["ver-line"]}></div>
                        <div className={classes["hor-line"]}></div>
                    </div>
                    <div className={classes.modal}>
                        <Inp type="text" holder="Name"/>
                        <Inp type="text" holder="Image"/>
                        <Button>Add</Button>
                    </div>
                </div>
            </div>
        );
    }
}

export default Order;