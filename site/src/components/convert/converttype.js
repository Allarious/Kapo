import React, {Component} from 'react';

import classes from './converttype.css';
import Button from './../buttons/authbutton';
import Inp from './../inputs/input';

let rToD = 0;
let dToR = 0;

class ConvertType extends Component{

    changeRtoD = (event) => {
        rToD = event;
    };
    returnRtoD = () => {
        return rToD;
    };

    changeDtoR = (event) => {
        dToR = event;
    };
    returnDtoR = () => {
        return dToR;
    };

    render() {
        let image = <div></div>
        let charge = "";
        let explain = "";
        let converter = <div></div>

        if (this.props.index === 0) {
            image = <div className={classes.logo}></div>
            charge = "Charge";
            explain = "Charge your wallet";
            converter = (<div>
                <Inp type="number" holder="Amount to charge (R)"/>
                <div className={classes.gap}></div>
            </div>)
        } else if (this.props.index === 1) {
            image = <div className={classes.logo1}></div>
            charge = "Change";
            explain = "Change from Rial to Dollar";
            converter = (<div>
                <Inp type="number" holder="Amount to change (R)" timeToChange={this.returnDtoR} changed={this.changeRtoD}/>
                <div className={classes.to}>To :</div>
                <Inp type="number" holder="Amount to charge ($)" timeToChange={this.returnRtoD} changed={this.changeDtoR}/>
            </div>)
        } else if (this.props.index === 2) {
            image = <div className={classes.logo2}></div>
            charge = "Change";
            explain = "Change from Rial to Euro";
            converter = (<div>
                <Inp type="number" holder="Amount to change (R)"/>
                <div className={classes.to}>To :</div>
                <Inp type="number" holder="Amount to charge (E)"/>
            </div>)
        }
        return (<div className={classes.content}>
            {image}
            <div className={classes.remain}>
                Remains : {this.props.remain}
            </div>
            <div className={classes.explain}>
                {explain}
            </div>
            {converter}
            <Button>{charge}</Button>
        </div>);
    }

}



export default ConvertType;