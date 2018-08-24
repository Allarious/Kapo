import React, { Component } from 'react';
import classes from './input.css';

// const Input = (props) => {
//     state = {
//         hello,
//     }
//     val = props.vl;
//     return (
      {/*<div>*/}
          {/*<input className={classes["login-input"]} type={props.type} placeholder={props.holder} value={val} onChange={(event) => {val = event}}/>*/}
       // </div>
     // );
 // };

class Input extends Component{

          state = {
              text: "",
          };

          onTodoChange(value){
              this.setState({
                 text: value
              });
          }

          render(){
              return (
                  <div>
                      <input className={classes["login-input"]}
                             type={this.props.type}
                             placeholder={this.props.holder}
                             value={this.state.text}
                             onChange={(event) => {
                                 this.onTodoChange(event.target.value);
                                 if (this.props.change!= undefined && this.props.change != "") {
                                     this.props.changed(event.target.value);
                                     // this.setState({ text :this.props.timeToChange()});
                                 }
                             }}/>
                  </div>
              );
          }
}

export default Input;