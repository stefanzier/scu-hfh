# SMScape

A Flask Application designed to provide a chatbot service for natural disaster victims in the form of both preparational and post-disaster assitance.

This application uses the Twilio API for SMS communication and represents the Chatbot Messaging Workflow as a Directed Graph Data Structure.

## Graph Data Structure Workflow

### Implementation 

We decided to represent the workflow of our chatbot as a directed graph. A user would begin at Node 0 which would provide the message

> This text is from TextToSaveYourLife. A hurricane is coming your way
> in the next 36 hours. Our system says you currently live in zipcode %.
> Text (1) if you still live here (2) to update your zipcode

From here our Flask backend integrated with the Twilio API processes user responses, and updates the user state to the appropriate Node in our graph.

We represented nodes as either "Questions" or "Answers" and provided the generic class *Option*  to handle both. 

This class definition is available here: https://github.com/stefanzier/scu-hfh/blob/master/classes/option.py.

In our graph, the functionality of questions is to send text to users via Twilio and options to execute some functionality to update either the nodes' state (i.e. whether a location's capacity is full) or the user's member variables (i.e. the zip code of a user).

Therefore the users state always starts of at a question. Upon receiving a SMS response from a user, our Flask handler method, updates the state to an option and executes the functionality of that option. The state then goes to the only next node that an option points to. This is a question. The user is given the text of the question our current state points to. 

This class definition of our graph available here: https://github.com/stefanzier/scu-hfh/blob/master/classes/graph.py.

### Visualization

A visualization of our graph is demonstrated below. It was done in vis.js. 

![Graph Representation of Chatbot Workflow](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/visualization/graph.png)

### Letting Third Parties Create Unique and Dynamic Graphs

Our application was designed to let third parties, such as the Red Cross or independent hospitals, to upload their own chat bot workflows to our application and present unique functionality to users. We provided a mechanism of letting them upload csv files, in which messages point to the next message in a workflow. The first 7 lines of our csv file for a hurricane workflow is shown below.

        0,This text is from TextToSaveYourLife. A hurricane is coming your way in the next 36 hours. Our system says you currently live in zipcode %. Text (1) if you still live here (2) to update your zipcode,0,3,,16|18
        1,Now Text (1) Prepare (2) Get Help (3) To Go Back,0,0,,2|3|24
        2,"""1:prepare""",1,0,,4
        3,"""2:get help""",1,0,,20
        4,To Prepare: text for (1) Shelters (2) Evacuation Plans (3) Items you need (4) To Go Back,0,0,,5|6|7|31
        5,"""1:shelter""",1,0,,8
        6,"""2:evac plans""",1,0,,13
        7,"""3:items""",1,0,,15


## Twilio API

The Twilio API was utilized to allow our backend code to process incoming SMS messages from users and send text-based responses back to them.

View our implementation of this API at : https://github.com/stefanzier/scu-hfh/blob/master/app.py

## View the Presentation Slides

![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide01.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide02.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide03.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide04.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide05.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide06.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide07.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide08.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide09.png.png)
![slide1](https://raw.githubusercontent.com/stefanzier/scu-hfh/master/slides/Slide10.png.png)

