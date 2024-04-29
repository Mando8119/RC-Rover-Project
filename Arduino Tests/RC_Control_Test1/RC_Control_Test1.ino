#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>

const char* ssid = "RC-Rover Radio";
const char* password = "123456789";

Servo steer_servo;
Servo drive_esc;//ESC - Electronic Speed Controller | This is attached to the motor propelling the rover
                // 1000 Microseconds = Full speed Backwards (Motor spins Counterclockwise?)
                // 1500 microseconds = Neutral
                // 2000 Microseconds = Full speed Forward (Motor spins Clockwise?)

int steer_value, speed;
String packet;

WebServer server(80);  // Object to handle HTTP requests

void handleRoot() {
  if (server.method() == HTTP_POST) {
    String message = server.arg("plain");
   // Serial.println(message);
    server.send(200, "text/plain", "Received: " + message);
  } else {
    server.send(404, "text/plain", "Only POST supported");
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  Serial.print("AP IP address: ");
  Serial.println(WiFi.softAPIP());

  server.on("/", handleRoot);
  server.begin();
  Serial.println("HTTP server started");

  steer_servo.attach(4);
  drive_esc.attach(6);

  steer_servo.write(93);
  drive_esc.writeMicroseconds(1500);
}

void loop() {
  server.handleClient();
  packet = server.arg("plain");

  steer_value = 93;
  speed = 1500;

  sscanf(packet.c_str(), "%d %d", &steer_value, &speed);
  Serial.print("Steer: ");
  Serial.print(steer_value);
  Serial.print(" Speed: ");
  Serial.print(speed);
  Serial.print("\n");

  steer_servo.write(steer_value);
}
