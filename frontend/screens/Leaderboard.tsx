import React, { useEffect, useState } from 'react';
import { View, FlatList } from 'react-native';
import UserBadge from '../components/UserBadge';
import { getLeaderboard } from '../services/api';

interface User {
  id: number;
  name: string;
  dorm: string;
  xp: number;
  karma: number;
}

export default function Leaderboard() {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    getLeaderboard().then((res: any) => setUsers(res.data));
  }, []);

  return (
    <View>
      <FlatList
        data={users}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }: { item: User }) => (
          <UserBadge
            name={item.name}
            dorm={item.dorm}
            xp={item.xp}
            karma={item.karma}
            badge="Speed Demon" // placeholder until badge_engine is integrated
          />
        )}
      />
    </View>
  );
}
