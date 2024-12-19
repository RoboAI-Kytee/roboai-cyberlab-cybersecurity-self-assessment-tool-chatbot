# Project Name

## Overview

This project is a Fastify server that integrates with OpenAI's API to stream text responses. It uses several npm packages to handle server operations, environment variables, and CORS.

## Prerequisites

- Node.js (version 20 or higher recommended)
- npm (Node Package Manager)

## Installation

1. Clone the repository:

   ````bash
   git clone <repository-url>
   cd <repository-directory>   ```

   ````

2. Install the dependencies:

   ````bash
   npm install   ```

   ````

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ````
   OPENAI_API_KEY=your_openai_api_key_here   ```
   ````

## Usage

1. Start the server:

   ````bash
   node server.js   ```

   ````

2. The server will run on `http://localhost:8080`. You can send a POST request to the root endpoint `/` with a JSON body containing a `prompt` field to receive a streamed text response.

3. Test the server with `curl`:

   `````bash
   curl -N -X POST -H "Content-Type: application/json" -d '{"prompt":"write a poem"}' http://localhost:8080   ````

   Example output:

   ```
   Certainly! Here's a short poem for you:

   ---

   In the hush of dawn's embrace,
   Whispers dance on morning's face.
   Golden rays through branches weave,
   Secrets that the night must leave.

   Dewdrops cling to blades of green,
   Reflecting worlds yet unseen.
   Birds compose their morning song,
   Nature's choir, pure and strong.

   The world awakes with gentle grace,
   In the sun's warm, tender chase.
   Moments fleeting, yet so dear,
   In the heart, they linger near.

   ---

   I hope you enjoyed it! If you have a specific theme or style in mind, feel free to let me know.   ```
   `````

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
