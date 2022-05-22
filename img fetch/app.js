const express  = require('express');
const mongoose = require('mongoose');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const app = express();

app.use(express.urlencoded({extended: true}));
app.use(express.json());
app.use(express.static('public'));

mongoose.connect('mongodb://localhost:27017/demo');

const connection = mongoose.connection;

var imageSchema = new mongoose.Schema({
    name: {
        type:String,
        required: true
    },
    imageData:
    {
        data: Buffer,
        contentType: String
    }
});

const imageModel = connection.model('pics',imageSchema);
  
var storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'images')
    },
    filename: (req, file, cb) => {
        cb(null, file.fieldname + '-' + Date.now())
    }
});
  
var upload = multer({ storage: storage });

app.post('/img', upload.single('image'), (req, res, next) => {
    
    var obj = {
        name: req.body.name,
        imageData: {
            data: fs.readFileSync(path.join(__dirname + '/images/' + req.file.filename)),
            contentType: 'image/png'
        }
    }
    imageModel.create(obj, (err, item) => {
        if (err) 
            console.log(err);
        
        else 
            res.send('Done');
        
    });
});

app.get('/getimage', (req, res) => {
    imageModel.find({}, (err, items) => {
        if (err) 
            console.log(err);
        else {
            let obj = {
                data: items[0].imageData.data.toString('base64')
            };
            res.json(obj);
        }
    });
});

app.listen(3000,() => {console.log('server started at 3000')});