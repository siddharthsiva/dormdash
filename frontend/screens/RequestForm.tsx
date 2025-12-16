import React, { useState } from 'react';
import { View, TextInput, Button } from 'react-native';
import { createRequest } from '../services/api';

export default function RequestForm() {
  const [item, setItem] = useState('');
  const [location, setLocation] = useState('');
  const [urgency, setUrgency] = useState('');
  const [reward, setReward] = useState('');

  const submitRequest = () => {
    createRequest({ item, location, urgency, reward: parseInt(reward), requester_id: 1 });
  };

  return (
    <View>
      <TextInput placeholder="Item" value={item} onChangeText={setItem} />
      <TextInput placeholder="Location" value={location} onChangeText={setLocation} />
      <TextInput placeholder="Urgency" value={urgency} onChangeText={setUrgency} />
      <TextInput placeholder="Reward" value={reward} onChangeText={setReward} keyboardType="numeric" />
      <Button title="Submit Request" onPress={submitRequest} />
    </View>
  );
}
