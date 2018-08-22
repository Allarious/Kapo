import React, { Component } from 'react';

import classes from './App.css';

import Navbar from '../components/navbar';
import Footer from '../components/footer';
import Login from '../components/login'
import ResetPassword from '../components/resetpassword';
import SignUp from '../components/signup';
import HomePage from '../components/homepage';
import Profile from '../components/profile';
import EditProfile from '../components/editprofile';

class App extends Component {

    state = {
      visiblePage: 'Homepage',
    };

    generateContent = () => {
        if (this.state.visiblePage === 'Homepage')
        {
            return <HomePage/>;
        } else if (this.state.visiblePage === 'Login')
        {
            return <Login clicked={this.changePage}/>;
        } else if(this.state.visiblePage === 'Signup')
        {
            return <SignUp/>;
        } else if(this.state.visiblePage === 'ForgetPassword')
        {
            return <ResetPassword/>;
        } else if(this.state.visiblePage === 'Profile')
        {
            return <Profile clicked={this.changePage}/>;
        }
        else if(this.state.visiblePage === 'EditProfile')
        {
            return <EditProfile/>;
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
