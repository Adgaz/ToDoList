export interface TodoItem {
    id: number;
    title: string;
    description: string | null;
    isCompleted: boolean;
    createdAt: Date;
    completedAt: Date | null;
}
