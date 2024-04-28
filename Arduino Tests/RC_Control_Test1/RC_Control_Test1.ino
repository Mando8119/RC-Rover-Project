#include <WiFi.h>
#include <WebServer.h>
#include <Servo.h>

const char* ssid = "RC-Rover Radio";
const char* password = "123456789";

Servo steer;
Servo drive_esc;//ESC - Electronic Speed Controller | This is attached to the motor propelling the rover
                // 1000 Microseconds = Full speed Backwards (Motor spins Counterclockwise?)
                // 1500 microseconds = Neutral
                // 2000 Microseconds = Full speed Forward (Motor spins Clockwise?)

int Steer_Position = 0;

WebServer server(80);  // Object to handle HTTP requests

void setup() {
  Serial.begin(115200);

  //Set up RC car servos and ESC
  steer.attach(4);
  drive_esc.attach(5);

  steer.write(93); //this is original straight position for servo
  drive_esc.writeMicroseconds(1500); //neutral for drive motor

  // Set up the ESP32 as an access point
  WiFi.softAP(ssid, password);
  Serial.println("Access Point Started");

  // Print the IP address of the ESP32
  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  // Define web server routes
  server.on("/", handleRoot);      // Call handleRoot when a client requests URI "/"
  server.begin();                  // Start the server
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();           // Handle client requests
}

// Handler for the root path
void handleRoot() {
  server.send(200, "text/plain", "Hello from ESP32!"); // Connect to server via local ip: 192.168.4.1
}

