#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>

const char* ssid = "RC-Rover Radio";
const char* password = "123456789";

Servo steer_servo;
Servo drive_esc;
int steer_value = 93, speed = 1500;  // Default values
String packet;

WebServer server(80);

void handleRoot() {
  if (server.method() == HTTP_POST) {
    String message = server.arg("plain");
    sscanf(message.c_str(), "%d %d", &steer_value, &speed);
    Serial.print("Received - Steer: ");
    Serial.print(steer_value);
    Serial.print(", Speed: ");
    Serial.println(speed);
    server.send(200, "text/plain", "Received: " + message);
  } else {
    server.send(404, "text/plain", "Only POST supported");
  }
}

void displayValues() {
  String html = "<!DOCTYPE html><html><head><title>RC Rover Status</title></head><body>";
  html += "<h1>RC Rover Control Values</h1>";
  html += "<p>Steer Value: " + String(steer_value) + "</p>";
  html += "<p>Speed: " + String(speed) + "</p>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  Serial.print("AP IP address: ");
  Serial.println(WiFi.softAPIP());

  server.on("/", handleRoot);
  server.on("/status", displayValues);
  server.begin();
  Serial.println("HTTP server started");

  steer_servo.attach(4);
  drive_esc.attach(5);
  steer_servo.write(steer_value);
  drive_esc.writeMicroseconds(speed);
}

void loop() {
  server.handleClient();
}