import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function RequestCard({ item, dorm, urgency, reward }: { item: string, dorm: string, urgency: string, reward: number }) {
  return (
    <View style={styles.card}>
      <Text style={styles.item}>{item}</Text>
      <Text>{dorm} • {urgency}</Text>
      <Text>Reward: {reward} XP</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 12, margin: 8, backgroundColor: '#f5f5f5', borderRadius: 8 },
  item: { fontSize: 18, fontWeight: 'bold' }
});
