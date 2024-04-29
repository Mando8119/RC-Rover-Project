#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "RC-Rover Radio";
const char* password = "123456789";

WebServer server(80);

void handleRoot() {
  if (server.method() == HTTP_POST) {
    String message = server.arg("plain");
    Serial.println("Received: " + message);
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
}

void loop() {
  server.handleClient();
}
