import {openai} from "@ai-sdk/openai";
import {streamText} from "ai";
import Fastify from "fastify";
import dotenv from "dotenv";
import cors from "@fastify/cors";

// Load environment variables
dotenv.config();

const fastify = Fastify({logger: true});

// Register CORS plugin
fastify.register(cors, {
  origin: "*",
});

// Ensure the API key is retrieved from the environment variable
const apiKey = process.env.OPENAI_API_KEY;

if (!apiKey) {
  console.error("OPENAI_API_KEY is not set in the environment variables");
  process.exit(1);
}

fastify.post("/", async function (request, reply) {
  const {prompt} = request.body;
  console.log(prompt, "prompt");

  const result = streamText({
    model: openai("gpt-4o"),
    prompt: prompt,
    apiKey,
  });

  reply.header("Content-Type", "text/plain; charset=utf-8");

  return reply.send(result.textStream);
});

fastify.listen({port: 8080});
