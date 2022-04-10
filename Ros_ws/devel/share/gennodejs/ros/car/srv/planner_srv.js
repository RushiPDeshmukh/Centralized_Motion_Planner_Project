// Auto-generated. Do not edit!

// (in-package car.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class planner_srvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.start = null;
      this.end = null;
    }
    else {
      if (initObj.hasOwnProperty('start')) {
        this.start = initObj.start
      }
      else {
        this.start = 0;
      }
      if (initObj.hasOwnProperty('end')) {
        this.end = initObj.end
      }
      else {
        this.end = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type planner_srvRequest
    // Serialize message field [start]
    bufferOffset = _serializer.int64(obj.start, buffer, bufferOffset);
    // Serialize message field [end]
    bufferOffset = _serializer.int64(obj.end, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type planner_srvRequest
    let len;
    let data = new planner_srvRequest(null);
    // Deserialize message field [start]
    data.start = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [end]
    data.end = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'car/planner_srvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd05166f308d494a305f8625733dd9f66';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 start
    int64 end
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new planner_srvRequest(null);
    if (msg.start !== undefined) {
      resolved.start = msg.start;
    }
    else {
      resolved.start = 0
    }

    if (msg.end !== undefined) {
      resolved.end = msg.end;
    }
    else {
      resolved.end = 0
    }

    return resolved;
    }
};

class planner_srvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.path = null;
    }
    else {
      if (initObj.hasOwnProperty('path')) {
        this.path = initObj.path
      }
      else {
        this.path = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type planner_srvResponse
    // Serialize message field [path]
    bufferOffset = _serializer.int64(obj.path, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type planner_srvResponse
    let len;
    let data = new planner_srvResponse(null);
    // Deserialize message field [path]
    data.path = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'car/planner_srvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5a0021da7e7b2bc0d903fa21ea74c6df';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 path
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new planner_srvResponse(null);
    if (msg.path !== undefined) {
      resolved.path = msg.path;
    }
    else {
      resolved.path = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: planner_srvRequest,
  Response: planner_srvResponse,
  md5sum() { return '1d89cdb41487474b11205506e2f1ce37'; },
  datatype() { return 'car/planner_srv'; }
};
