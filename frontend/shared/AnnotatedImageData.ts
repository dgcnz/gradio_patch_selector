import type { FileData } from "@gradio/client";

export default class AnnotatedImageData {
    image: FileData;
    patchIndex: number | null = null;
}
