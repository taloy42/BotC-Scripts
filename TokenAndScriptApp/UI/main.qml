import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 800
    height: 800
    title: "HelloApp"
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "C:\\Users\\anukh\\Downloads\\BotC\\repository\\BotC-Scripts\\TokenAndScriptApp\\images\\img.webp"
            fillMode: Image.PreserveAspectCrop
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: "16:38:33"
                font.pixelSize: 24
                color: "white"
            }
        }
    }
}