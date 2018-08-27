import React, {Component} from 'react';

import classes from './App.css';

import Navbar from '../components/navbar';
import Footer from '../components/footer';
import Login from '../components/login'
import ResetPassword from '../components/resetpassword';
import SignUp from '../components/signup';
import HomePage from '../components/homepage';
import Profile from '../components/profile';
import EditProfile from '../components/editprofile';
import SendMessage from '../components/sendmessage';
import Conv from '../components/convert';
import Error from '../components/error'
import Accounts from '../components/accounts';
import Dashboard from '../components/dashboard';
import Order from '../components/order';
import FillExam from '../components/order/fillexam';

class App extends Component {

    state = {
        visiblePage: 'Homepage',
    };

    generateContent = () => {
        if (this.state.visiblePage === 'Homepage') {
            return <HomePage/>;
        } else if (this.state.visiblePage === 'Login') {
            return <Login clicked={this.changePage}/>;
        } else if (this.state.visiblePage === 'Signup') {
            return <SignUp clicked={this.changePage}/>;
        } else if (this.state.visiblePage === 'ForgetPassword') {
            return <ResetPassword/>;
        } else if (this.state.visiblePage === 'Profile') {
            return <Profile clicked={this.changePage}/>;
        } else if (this.state.visiblePage === 'EditProfile') {
            return <EditProfile/>;
        } else if (this.state.visiblePage === 'SendMessage') {
            return <SendMessage/>;
        } else if (this.state.visiblePage === 'Convert') {
            return <Conv/>;
        } else if (this.state.visiblePage === 'Error') {
            return <Error clicked={this.changePage}/>;
        } else if (this.state.visiblePage === 'Accounts') {
            return <Accounts/>;
        } else if (this.state.visiblePage === 'Dashboard') {
            return <Dashboard/>;
        } else if (this.state.visiblePage === 'Order') {
            return <Order clicked={this.changePage}/>;
        } else if (this.state.visiblePage === 'Fill Exam') {
            return <FillExam/>;
        } else {
            return <Error clicked={this.changePage}/>;
        }
    };

    changePage = (pageName) => {
        this.setState({visiblePage: pageName});
    };

    render() {

        return (
            <div className={classes.App}>
                <Navbar clicked={this.changePage}/>
                {this.generateContent()}
                <Footer/>
            </div>
        );
    }
}

export default App;
