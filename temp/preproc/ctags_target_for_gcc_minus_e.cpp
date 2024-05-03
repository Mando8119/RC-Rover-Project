# 1 "C:\\Users\\Worst\\OneDrive\\Desktop\\RC-Rover-Project\\Arduino Tests\\RC_Control_Test1\\RC_Control_Test1.ino"
# 2 "C:\\Users\\Worst\\OneDrive\\Desktop\\RC-Rover-Project\\Arduino Tests\\RC_Control_Test1\\RC_Control_Test1.ino" 2
# 3 "C:\\Users\\Worst\\OneDrive\\Desktop\\RC-Rover-Project\\Arduino Tests\\RC_Control_Test1\\RC_Control_Test1.ino" 2
# 4 "C:\\Users\\Worst\\OneDrive\\Desktop\\RC-Rover-Project\\Arduino Tests\\RC_Control_Test1\\RC_Control_Test1.ino" 2

const char* ssid = "RC-Rover Radio";
const char* password = "123456789";

Servo steer_servo;
Servo drive_esc;
int steer_value = 93, speed = 1500; // Default values
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
  } else if (server.method() == HTTP_GET) {
    server.send(200, "text/html", displayValues());
  }
}

String displayValues() {
  String html = "<!DOCTYPE html><html><head><title>RC Rover Status</title></head><body>";
  html += "<h1>RC Rover Control Values</h1>";
  html += "<p id='steer'>Steer Value: " + String(steer_value) + "</p>";
  html += "<p id='speed'>Speed: " + String(speed) + "</p>";
  html += "<script>";
  html += "setInterval(function() {";
  html += "fetch('/data').then(response => response.json()).then(data => {";
  html += "document.getElementById('steer').textContent = 'Steer Value: ' + data.steer;";
  html += "document.getElementById('speed').textContent = 'Speed: ' + data.speed;";
  html += "});";
  html += "}, 250);"; // Update every quarter-second
  html += "</script>";
  html += "</body></html>";
  return html;
}

void handleData() {
  String json = "{";
  json += "\"steer\":"; json += steer_value; json += ",";
  json += "\"speed\":"; json += speed;
  json += "}";
  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  Serial.print("AP IP address: ");
  Serial.println(WiFi.softAPIP());

  server.on("/", handleRoot);
  server.on("/status", displayValues);
  server.on("/data", handleData);
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
