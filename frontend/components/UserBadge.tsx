import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface UserBadgeProps {
  name: string;
  dorm: string;
  xp: number;
  karma: number;
  badge: string;
}

export default function UserBadge({ name, dorm, xp, karma, badge }: UserBadgeProps) {
  return (
    <View style={styles.badge}>
      <Text style={styles.name}>{name}</Text>
      <Text>{dorm}</Text>
      <Text>XP: {xp} • Karma: {karma}</Text>
      <Text style={styles.badgeText}>{badge}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  badge: { padding: 10, margin: 6, backgroundColor: '#e0f7fa', borderRadius: 8 },
  name: { fontWeight: 'bold' },
  badgeText: { color: '#00796b', fontWeight: '600' }
});
