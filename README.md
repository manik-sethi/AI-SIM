# Purpose 
Brainslice's purpose is to provide insight on how neural networks work, and what is actually going on. Those unfamiliar with neural networks will be able to see how the machine learns in live action.

# How I think the project will work
---
## Frontend
Our app only needs one page. On the page, users should be able to experiment. One example of the layout is this.
![[Pasted image 20231026092806.png]] 
There will be some feature that enables changing the parameters of the task. Looking at the figure above, we can see that changing the parameters of the task means changing the map.
![[Pasted image 20231026092932.png]]
*Notice how since the map changed, so did the functions of it's neurons, represented by color*

The highlight of this page will be the "brainslice" display. The neural network we use to train the model will be displayed on the screen. Understandably, the *actual* neural network may be a lot more complex, so we may use a simplified version that is still comprehensive.

There are 2 main components to this app. The task being learned, and the demonstration of learning. 

1. Firstly, let's discuss the task being learned. Simply put, it will be a simulation in the web page that the user will input. For example purposes, let's assume the task being learned is how to complete a race track quickly. Other examples can be gambling simulator, cross-y road simulator, anything game like. If we give it new racetracks, we should see the computer trying to learn it



2. Secondly, the highlight of this page will be the "brainslice" display. The neural network we use to train the model will be displayed on the screen. Understandably, the *actual* neural network may be a lot more complex, so we may use a simplified version that is still comprehensive. As the computer is learning a new task, we should see the brainslice display change numbers and colors to signify a change in the cognitive process

 
## Backend

Unlike other projects we have made, this can't be just a mock website that only exists in our github repositories. Rather, it will have to be hosted so client-side users can access it on the web and run simulations using our server. As of right now, I cannot offer much judgement on how complex the backend will be. Right now, I can only foresee API calls for changing the appearance of brainface, showing the model learning, and adjusting parameteres.


---
# Needs
* Only one tab needed, BrainSlice Page
* Hosted online, cannot be a mock website
* Task simulator
* Visualization of the machine going through the task
* Ability to switch tasks
* Brainslice display
* The ability to see something about the display changing, numerically and physically
	* Physically, it should be something easier on the eyes like color or size

In essence, anything that shows us *how* the process is occurring is almost certainly necessary for the purpose of this project.
# Wants
* A landing page with a whole rundown of the project
* The ability to adjust the display of brainslice display, make it more convoluted vs simplified
* The ability to "retroactively learn" 
	* Instead of the task causing an effect on the brainslice, we can manually change some characteristic of a neuron in brainslice, and see how our neuron behaves.





# Buzzwords

Machine Learning
Brain modeling
Data visualization
Data processing
Tensorflow or pytorch
Fullstack
Dynamic website
