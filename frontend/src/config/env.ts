const LOCAL_HOST = "localhost";

const DEFAULT_API_PORT = 5000;
const DEFAULT_NATS_PORT = 1234;

export const API_BASE_URL =
  import.meta.env.VITE_API_URL ?? `http://${LOCAL_HOST}:${DEFAULT_API_PORT}`;

export const NATS_BASE_URL =
  import.meta.env.VITE_NATS_URL ?? `ws://${LOCAL_HOST}:${DEFAULT_NATS_PORT}`;
