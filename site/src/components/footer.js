import React from 'react';

import classes from './footer/footer.css';
import ContactUs from './footer/contactUs';
import EmailUs from './footer/emailUs';
import FollowUs from './footer/followUs';
import MeetUs from './footer/meetUs';

const Footer = () => {
  return <div className={classes.footer}>
    <div className={classes["footer-components"]}>
    <ContactUs/>
    </div>
      <div className={classes["footer-components"]}>
          <EmailUs/>
      </div>
      <div className={classes["footer-components"]}>
          <FollowUs/>
      </div>
      <div className={classes["footer-components"]}>
          <MeetUs/>
      </div>
  </div>
};

export default Footer;