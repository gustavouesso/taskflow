import { Injectable, OnModuleInit } from '@nestjs/common';

@Injectable()
export class TaskConsumerService implements OnModuleInit {
  async onModuleInit() {
    console.log('Listening to SQS for new tasks...');
    // Simula consumo de mensagens
    setInterval(() => {
      console.log('Received task event');
    }, 5000);
  }
}