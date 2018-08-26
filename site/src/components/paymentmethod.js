import React, {Component} from 'react';

import classes from './paymentmethod/paymentmethod.css';

class PaymentMethod extends Component{

    state = {currency: "Dollar"};

    content = <div></div>;

    clckd = (event) => {

        console.log(event);

        this.setState({currency: event});

    };

    render(){

        if (this.state.currency === "Rial")
        {
            this.content = (

                <div>
                    <div className={classes["rial-active"]} onClick={() => this.clckd("Rial")}></div>
                    <div className={classes.dollar} onClick={() => this.clckd("Dollar")}></div>
                    <div className={classes.euro} onClick={() => this.clckd("Euro")}></div>
                </div>

            );
        } else if(this.state.currency === "Dollar")
        {
            this.content = (

            <div>
                <div className={classes.rial} onClick={() => this.clckd("Rial")}></div>
                <div className={classes["dollar-active"]} onClick={() => this.clckd("Dollar")}></div>
                <div className={classes.euro} onClick={() => this.clckd("Euro")}></div>
            </div>
            );

        } else if(this.state.currency === "Euro")
        {

            this.content = (
            <div>
                <div className={classes.rial} onClick={() => this.clckd("Rial")}></div>
                <div className={classes.dollar} onClick={() => this.clckd("Dollar")}></div>
                <div className={classes["euro-active"]} onClick={() => this.clckd("Euro")}></div>
            </div>
            );

        }

        return(
            <div className={classes.container}>

                <div className={classes.header}> Choose A Payment Currency </div>

                <div className={classes["inner-container"]}>
                    {this.content}
                </div>

            </div>
        );
    }

};

export default PaymentMethod;