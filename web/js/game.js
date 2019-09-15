let maxHeight;
let maxWidth; 
let tileSize = 40;

let colors = [
  '#007bff',
  '#6c757d',
  '#28a745',
  '#17a2b8',
  '#ffc107',
  '#dc3545',
  '#f8f9fa',
  '#343a40',
];

function setup() {
  var cnv = createCanvas(800, 480);
  maxHeight = 480;
  maxWidth = 800; 
  var x = 149; //(windowWidth - width) / 2;
  var y = 67; //(windowHeight - height) / 2;
  cnv.position(x, y);
  background(255, 255, 255);
}
  
function draw() {
  //background(0)

  //const newGameButton = new Button(windowWidth/2 - 75, windowHeight/2 - 35, 150, 70); 
  //newGameButton.draw();
  //newGameButton.setText('NEW GAME');
 
  eel.setCanvasDimensions(maxHeight, maxWidth, tileSize);
  eel.createGameBoard()(initalConfig);
  noLoop(); 
}

function printX(data) {
  //console.log("X: " + data);
}

function printY(data) {
  //console.log("Y: " + data);
}

function initalConfig(size) {
  for(let indexA = 0; indexA < size[0]; indexA++) {
    for(let indexB = 0; indexB < size[1]; indexB++) {
      eel.getData(indexA, indexB)(drawBox);
    }
  }
}

function drawBox(data) {
  console.log(data[0]);
  console.log(data[1]);
  const demoBox = new Box(data[0], data[1], tileSize, tileSize, data[2]); 
  demoBox.draw();
}

// Creating my style buttons
function Box(locationX, locationY, width, height, color) {
  this.locationX = locationX; 
  this.locationY = locationY; 
  this.width = width; 
  this.height = height;
  this.color = color;
}

Box.prototype.getLocation = function() {
  return this.locationX, this.locationY;
}

Box.prototype.draw = function() {
  noStroke();
  fill(this.color);
  rect(this.locationX, this.locationY, this.width, this.height); 
}

function returnToMain() {
  window.open("../start.html", "_self");
}

/*
Button.prototype.setText = function(text) {
  textAlign(CENTER, CENTER)
  text(text, this.locationX, this.locationY, this.width);
}*/
