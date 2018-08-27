import React, {Component} from 'react';

import classes from './dashboard/dashboard.css';
import Messages from './dashboard/messages';
import MainPage from './dashboard/mainpage';
import Transactions from './dashboard/transactions';
import Orders from './dashboard/orders';

class Dashboard extends Component {

    state = {
        dashboardPages: [
            {id:'p1', name: 'Main Page', active:true,},
            {id:'p2', name: 'Messages', active:false,},
            {id:'p3', name: 'Transactions', active:false,},
            {id:'p4', name: 'Orders', active:false,}
        ],
        visiblePage: 'Main Page',
    };

    changeActive = (event) => {

        if (event === 0){
            this.setState({visiblePage:'Main Page'})
        } else if(event === 1){
            this.setState({visiblePage:'Messages'})
        }else if(event === 2){
            this.setState({visiblePage:'Transactions'})
        }else if(event === 3){
            this.setState({visiblePage:'Orders'})
        }
        this.setState({dashboardPages: [
                {id:'p1', name: 'Main Page', active: (event === 0) ,},
                {id:'p2', name: 'Messages', active: (event === 1) ,},
                {id:'p3', name: 'Transactions', active: (event === 2) ,},
                {id:'p4', name: 'Orders', active: (event === 3) ,}
            ]});

    };

    content = <div></div>


    render()
    {

        let nav = <div></div>
        if(this.state.visiblePage === 'Messages')
        {
            this.content = <Messages/>;
            nav = (        <div className={classes["nav-container"]}>
                <div className={classes["message-from"]}>from</div>
                <div className={classes["message-name"]}>name</div>
                <div className={classes["message-thumbnail"]}>thumbnail</div>
                <div className={classes["message-condition"]}>condition</div>
            </div>);
        } else if (this.state.visiblePage === 'Main Page')
        {
            this.content = <MainPage/>;
        } else if (this.state.visiblePage === 'Transactions')
        {
            this.content = <Transactions/>;
            nav = (<div className={classes["nav-container"]}>
                <div className={classes.left}>Username</div>
                <div className={classes.middle}>Type</div>
                <div className={classes.middle}>Cost</div>
                <div className={classes.middle}>Date</div>
                <div className={classes.middle}>Time</div>
                <div className={classes.right}>Condition</div>
            </div>);
        }else if (this.state.visiblePage === 'Orders')
        {
            this.content = <Orders/>;
            nav = (<div className={classes["nav-container"]}>
                <div className={classes.left}>Username</div>
                <div className={classes.middle}>Type</div>
                <div className={classes.middle}>Cost</div>
                <div className={classes.middle}>Date</div>
                <div className={classes.middle}>Time</div>
                <div className={classes.right}>Condition</div>
            </div>);
        } else {
            this.content = <MainPage/>;
        }

        let leftCol = (
            <div className={classes["left-col"]}>
                <div className={classes.logo}> Kapo </div>
                {this.state.dashboardPages.map((event, index) => {
                    if (event.active)
                    {
                        return <button key={event.id} className={classes["left-col-selectors-active"]} onClick={() => this.changeActive(index)}>{event.name}</button>;
                    }else {
                        return <button key={event.id} className={classes["left-col-selectors"]} onClick={() => this.changeActive(index)}>{event.name}</button>;
                    }
                })}
            </div>
        );

        return (
            <div className={classes.container}>
            {leftCol}
            <div className={classes["right-col"]}>
                    <div className={classes.nav}>
                        {nav}
                    </div>
                        <div className={classes["inner-container"]}>
                            {this.content}
                        </div>
                    </div>
                </div>);
    }
}

export default Dashboard;