import React from 'react';

import classes from './messages.css';
import MessageComponent from './messagecomponents';

const Messages = () => {

    const messages = [
        {
            id:'m1',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m2',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m3',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m4',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m5',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m6',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m7',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m8',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },{
            id:'m9',
            name:'About IELTS',
            from:'Manager',
            thumbnail:'Hello and Good Evening ...',
            message:'Lorem ipsum dolor sit amet, nam in eirmod sapientem dissentias, et duo nostrum platonem qualisque. Quaestio intellegat assueverit his cu. Te nam maiorum percipitur deterruisset, pri ex tibique epicurei vivendum. Eum choro molestiae omittantur ad, congue maiorum accumsan sed id. Dicant omnesque deterruisset in quo, no eam sumo audiam.\n' +
            '\n' +
            'No eum cibo quando efficiendi, vix ei quis putant. Eu sea modo dolore altera, minim iudico eloquentiam cu nec, ad vim dolorum ullamcorper. Persius eleifend vix id. Ius munere tamquam percipit eu, eum illum delectus inimicus cu. Ad mnesarchum philosophia cum, sed an oblique nostrum.',
        },
    ];



    return (
        <div className={classes.container}>
            <div className={classes.hovercancel}></div>
            {messages.map((event) => {
                return (
                    <MessageComponent key={event.id}
                                    name={event.name}
                                    from={event.from}
                                    thumbnail={event.thumbnail}
                                    message={event.message}
                                    condition="Read"/>
                );
            })}
        </div>
    );

};

export default Messages;