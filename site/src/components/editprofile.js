import React from 'react';

import classes from './profile/editprofile.css';

const EditProfile = () => {
    return(
        <div>

        <form className="form">
            <h2>User Profile</h2>
            <div className="form-group">
                <label htmlFor="email">Full Name:</label>
                <div className="relative">
                    <input className="form-control" id="name" type="text" pattern="[a-zA-Z\s]+" required="" autoFocus=""
                           title="Username should only contain letters. e.g. Piyush Gupta" autoComplete=""
                           placeholder="Type your name here...">
                        <i className="fa fa-user"></i>
                </div>
            </div>
            <div className="form-group">
                <label htmlFor="email">Email address:</label>
                <div className="relative">
                    <input className="form-control" type="email" required="" placeholder="Type your email address..."
                           pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$">
                        <i className="fa fa-envelope"></i>
                </div>
            </div>
            <div className="form-group">
                <label htmlFor="email">Contact Number:</label>
                <div className="relative">
                    <input className="form-control" type="text" maxLength="10"
                           onInput="this.value=this.value.replace(/[^0-9]/g,'');" required=""
                           placeholder="Type your Mobile Number...">
                        <i className="fa fa-phone"></i>
                </div>
            </div>
            <div className="form-group">
                <label htmlFor="email">Company Name:</label>
                <div className="relative">
                    <input className="form-control" type="url" pattern="https?://.+" required=""
                           placeholder="Mention your company link(url)...">
                        <i className="fa fa-building"></i>
                </div>
            </div>
            <div className="form-group">
                <label htmlFor="email">Designation:</label>
                <div className="relative">
                    <input className="form-control" type="text" id="designation" required=""
                           placeholder="Type your designation...">
                        <i className="fa fa-suitcase"></i>
                </div>
            </div>
            <div className="form-group">
                <label htmlFor="email">Specilization:</label>
                <div className="relative">
                    <input className="form-control" type="text" id="tags" required=""
                           placeholder="Type your specialization...">
                        <i className="fa fa-css3"></i>
                </div>
            </div>
            <div className="form-group">
                <label htmlFor="email">Attachment:</label>
                <div className="relative">
                    <div className="input-group">
                        <label className="input-group-btn">
            <span className="btn btn-default">
                Browse&hellip; <input type="file" style="display: none;" multiple>
            </span>
                        </label>
                        <input type="text" className="form-control" required="" placeholder="Attachment..." readOnly>
                            <i className="fa fa-link"></i>
                    </div>
                </div>
            </div>

            <div className="tright">
                <a href="">
                    <button className="movebtn movebtnre" type="Reset"><i className="fa fa-fw fa-refresh"></i> Reset
                    </button>
                </a>
                <a href="">
                    <button className="movebtn movebtnsu" type="Submit">Submit <i
                        className="fa fa-fw fa-paper-plane"></i></button>
                </a>
            </div>
        </form>

        <div className="thanks" style="display: none;">
            <h4>Thank you!</h4>
            <p>
                <small>Your message has been successfully sent.</small>
            </p>
        </div>
        <!--<script src='https://code.jquery.com/jquery-1.12.4.js'></script>-->
        <!--<script src='https://code.jquery.com/ui/1.12.1/jquery-ui.js'></script>-->
        <!---->
        <!---->
        <!---->
        <!--<script  src="js/index.js"></script>-->


        </div>
    );
};