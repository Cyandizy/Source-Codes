#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <nlohmann/json.hpp>
#include "upper.hpp"
using json = nlohmann::json;

class ToDoList {
    private:
        bool programRunning = true;
        std::unordered_map<std::string, std::string> tasksData;

    public:
        void addTask() {
            std::string newTask;
            std::cout << "taskName> ";
            std::getline(std::cin, newTask);
            tasksData[newTask] = "undone";
            std::cout << "The task has been added.\n";
            saveTasks();
        }

        void showTasks() {
            for (const auto entry : tasksData){
                std::cout << entry.first << " [" << entry.second << "]\n";
            }
        }

        void updateTask() {
            bool foundTask = false;
            std::string taskName;
            std::cout << "taskName>";
            std::getline(std::cin, taskName);
            for (const auto entry : tasksData){
                if (keywordFound(upper(taskName), entry.first)) {
                    foundTask = true;
                    if (entry.second == "undone") {
                        tasksData[entry.first] = "done";
                    }
                    else if (entry.second == "done") {
                        tasksData[entry.first] = "undone";
                    }
                }
            }
            if (foundTask) {
                saveTasks();
                std::cout << "The task has been updated.\n";
            }
            else if (!foundTask) {
                std::cout << "The task with this name is not found.\n";
            }
        }

        void deleteTask() {
            bool foundTask = false;
            std::string taskName;
            std::cout << "taskName>";
            std::getline(std::cin, taskName);
            for (auto entry : tasksData){
                if (keywordFound(upper(taskName), entry.first)) {
                    foundTask = true;
                    tasksData.erase(entry.first);
                    break;
                }
            }
            if (foundTask) {
                saveTasks();
                std::cout << "The task has been deleted.\n";
            }
            else if (!foundTask) {
                std::cout << "The task with this name is not found.\n";
            }
        }        

        void loadTasks() {
            std::ifstream file("data.json");
            json data = json::parse(file);
            tasksData = data.get<std::unordered_map<std::string, std::string>>();
        }

        void saveTasks() {
            json data;
            for (const auto entry : tasksData) {
                data[entry.first] = entry.second;
            }
            std::ofstream file("data.json");
            file << data;
        }

        void interface() {
            std::string userCommand;
            while (programRunning) {
                std::cout << "ToDoList>";
                std::getline(std::cin, userCommand);
                if (keywordFound("QUIT", userCommand)) {
                    std::clog << "The program has stopped.";
                    quitProgram();
                    break;
                }
                else if (keywordFound("ADD", userCommand) || keywordFound("NEW", userCommand)) {
                    addTask();
                }
                else if (keywordFound("SHOW", userCommand)) {
                    showTasks();
                }
                else if (keywordFound("UPDATE", userCommand)) {
                    updateTask();
                }
                else if (keywordFound("DELETE", userCommand)) {
                    deleteTask();
                }
                else {
                    std::clog << "Nothing happened. (You typed \"" << userCommand << ")\"\n";
                }
            }
        }
        void startProgram() {
            std::cout << "ToDoList V1.0\n" << "The commands are \"add\", \"show\", \"update\", \"delete\".\n";
            loadTasks();
            interface();
        }

        void quitProgram() {
            programRunning = false;
        }

        bool keywordFound(const std::string_view keyword, const std::string str) {
            return upper(str).find(keyword) != std::string::npos;
        }
};

int main() {
    ToDoList program;
    program.startProgram();

    return 0;
}