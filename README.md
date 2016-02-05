# Bolos e Biscoitos da Cleo

Site shop for sales and orders for cakes and biscuits. Website also serves as catalog

## Site
- [Bolos e Biscoitos da Cleo](https://cleonice-prod.herokuapp.com/)

## Contact 
- [See contact forms on the web site](https://cleonice-prod.herokuapp.com/contato/)

## Social Networks
- [Facebook](https://www.facebook.com/BolosEBiscoitosDaCleo/)
- [Twiiter](https://twitter.com/cleobolos)

## Language and Frameworks
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Cloudinary](http://cloudinary.com/)

## FAQs
- leonardo.ncintra@outlook.com
- bolosdacleo@gmail.com


### Start with virtualenv

We recommend and support the usage of **virtualenv**. All you need to do is create a new virtualenv (if necessary):

    virtualenv venv

And then just activate it:

    source venv/bin/activate

This project depends on [Cloudinary's Python library](https://github.com/cloudinary/pycloudinary). 

## Installation

Run the following commands from your shell.

Project cloning and dependent package installation: 

    git clone https://github.com/leonardocintra/cleonice.git
    cd cleonice
    pip install -r requirements.txt

Defining Cloudinary's credentials. The CLOUDINARY_URL value is available in the [dashboard of your Cloudinary account](https://cloudinary.com/console). 
If you don't have a Cloudinary account yet, [click here](https://cloudinary.com/users/register/free) to creare your free acount.
     
    export CLOUDINARY_URL=cloudinary://<API-KEY>:<API-SECRET>@<CLOUD-NAME>

