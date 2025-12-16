import React, { useEffect, useState } from 'react';
import { View, FlatList } from 'react-native';
import RequestCard from '../components/RequestCard';
import { getRequests } from '../services/api';

interface Request {
  id: number;
  item: string;
  location: string;
  urgency: string;
  reward: number;
}

export default function HomeScreen() {
  const [requests, setRequests] = useState<Request[]>([]);

  useEffect(() => {
    getRequests().then((res: any) => setRequests(res.data));
  }, []);

  return (
    <View>
      <FlatList
        data={requests}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }: { item: Request }) => (
          <RequestCard
            item={item.item}
            dorm={item.location}
            urgency={item.urgency}
            reward={item.reward}
          />
        )}
      />
    </View>
  );
}
