import React, { useState } from 'react';
import { Chat, Bubble } from '@chatui/core';
import '@chatui/core/dist/index.css';

const ChatUI: React.FC = () => {
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState('');

  const handleSend = async (type: string, val: string) => {
    setMessages([...messages, { type: 'text', content: { text: val } }]);
    const res = await fetch('http://localhost:8000/agent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: val }),
    });
    const data = await res.json();
    setMessages((msgs) => [...msgs, { type: 'text', content: { text: data.response } }]);
  };

  return (
    <Chat
      navbar={{ title: 'ShopMind' }}
      messages={messages}
      renderMessageContent={(msg) => <Bubble content={msg.content.text} />} 
      onSend={handleSend}
      locale="en-US"
    />
  );
};

export default ChatUI;
