import { defineConfig } from "tinacms";

export default defineConfig({
  branch: "master",

  clientId: process.env.NEXT_PUBLIC_TINA_CLIENT_ID,
  token: process.env.TINA_TOKEN,

  build: {
    outputFolder: "admin",
    publicFolder: "output",
  },

  media: {
    tina: {
      mediaRoot: "",
      publicFolder: "content",
    },
  },

  // See docs on content modelling for more info on how to setup new content models: https://tina.io/docs/schema/
  schema: {
    collections: [
      {
        name: "blog",
        label: "Blog",
        path: "content/Blog",
        fields: [
          {
            name: "title",
            label: "Title",
            type: "string",
            isTitle: true,
            required: true,
          },
          {
            name: "date",
            label: "Date",
            type: "datetime",
            required: true,
          },
          {
            name: "content",
            label: "Content",
            type: "rich-text",
            isBody: true,
          },
        ],
      },
    ],
  },
});
