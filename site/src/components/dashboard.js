import React, {Component} from 'react';

import classes from './dashboard/dashboard.css';

class Dashboard extends Component {

    state = {
        dashboardPages: [
            {id:'p1', name: 'Main Page',},
            {id:'p2', name: 'Messages',},
            {id:'p3', name: 'Transactions',},
            {id:'p4', name: 'Orders',}
        ],
        visiblePage: 'dashboardMain',
    };

    leftCol = (
        <div className={classes["left-col"]}>
            <div className={classes.logo}></div>
            {this.state.dashboardPages.map((event) => {
                return <button className={classes["left-col-selectors"]}>{event.name}</button>;
            })}
        </div>
    );

    render()
    {
        return (<div className={classes.container}>
            {this.leftCol}
            <div className={classes["right-col"]}>
            <div className={classes.nav}></div>
            <div className={classes["inner-container"]}>
                <div className={classes["main-page-content"]}></div>
                <div className={classes["main-page-content"]}></div>
            </div>
            </div>
        </div>);
    }
}

export default Dashboard;