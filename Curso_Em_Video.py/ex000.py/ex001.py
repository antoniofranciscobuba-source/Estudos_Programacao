import uuid

class Task:
    """
    Representa uma única tarefa com descrição, um identificador único e status de conclusão.

    Atributos:
        task_id (str): Um identificador único para a tarefa.
        description (str): A descrição textual da tarefa.
        is_completed (bool): O status de conclusão da tarefa (True se concluída, False caso contrário).
    """

    def __init__(self, description: str, task_id: str) -> None:
        """
        Inicializa uma nova instância da classe Task.

        Args:
            description (str): A descrição da tarefa.
            task_id (str): O identificador único para a tarefa.
        """
        self.task_id = task_id
        self.description = description
        self.is_completed = False

    def __repr__(self) -> str:
        """
        Retorna a representação oficial da tarefa.
        """
        status = "Concluída" if self.is_completed else "Pendente"
        return f"Task(ID: {self.task_id}, Descrição: '{self.description}', Status: {status})"

class TaskManager:
    """
    Gerencia uma coleção de objetos Task, permitindo a adição e listagem de tarefas.

    Atributos:
        _tasks (list[Task]): Uma lista privada para armazenar os objetos Task.
    """

    def __init__(self) -> None:
        """
        Inicializa uma nova instância da classe TaskManager com uma lista vazia de tarefas.
        """
        self._tasks: list[Task] = []

    def add_task(self, description: str) -> Task:
        """
        Cria e adiciona uma nova tarefa à lista de tarefas gerenciadas.

        Args:
            description (str): A descrição da nova tarefa.

        Returns:
            Task: O objeto Task recém-criado e adicionado.
        """
        task_id = str(uuid.uuid4())  # Gera um ID único usando UUID
        new_task = Task(description, task_id)
        self._tasks.append(new_task)
        print(f"Tarefa adicionada: {new_task}")
        return new_task

    def get_all_tasks(self) -> list[Task]:
        """
        Retorna a lista completa de todas as tarefas gerenciadas.

        Returns:
            list[Task]: Uma lista contendo todos os objetos Task.
        """
        return self._tasks

    def get_task_by_id(self, task_id: str) -> Task | None:
        """
        Busca uma tarefa pelo seu ID único.

        Args:
            task_id (str): O ID único da tarefa a ser buscada.

        Returns:
            Task | None: O objeto Task se encontrado, caso contrário None.
        """
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        return None

    def mark_task_as_completed(self, task_id: str) -> bool:
        """
        Marca uma tarefa específica como concluída.

        Args:
            task_id (str): O ID único da tarefa a ser marcada como concluída.

        Returns:
            bool: True se a tarefa foi encontrada e marcada como concluída, False caso contrário.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.is_completed = True
            print(f"Tarefa {task.task_id} marcada como concluída.")
            return True
        print(f"Erro: Tarefa com ID '{task_id}' não encontrada.")
        return False

# Exemplo de uso (para teste)
if __name__ == "__main__":
    print("Criando um gerenciador de tarefas...")
    manager = TaskManager()

    print("\nAdicionando tarefas...")
    task1 = manager.add_task("Comprar leite")
    task2 = manager.add_task("Pagar contas")
    task3 = manager.add_task("Estudar Python")

    print("\nListando todas as tarefas:")
    for task in manager.get_all_tasks():
        print(task)

    print("\nMarcando uma tarefa como concluída...")
    if task2.task_id:
        manager.mark_task_as_completed(task2.task_id)

    print("\nListando todas as tarefas novamente:")
    for task in manager.get_all_tasks():
        print(task)

    print("\nTentando marcar uma tarefa inexistente...")
    manager.mark_task_as_completed("id_inexistente")
