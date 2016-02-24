#ifndef __VIZIA_DOOM_GAME_H__
#define __VIZIA_DOOM_GAME_H__

#include "ViziaDoomDefines.h"
#include "ViziaDoomController.h"

#include <string>
#include <vector>
#include <list>

namespace Vizia {

    class DoomGame {

    public:

        struct State {
            unsigned int number;
            std::vector<int> gameVariables;
            uint8_t * imageBuffer;
        };

        DoomGame();
        virtual ~DoomGame();

        bool loadConfig(std::string filename);

        bool init();
        void close();

        void newEpisode();
        bool isRunning();

        void setAction(std::vector<int> const &actions);
        void advanceAction();
        void advanceAction(unsigned int tics);
        void advanceAction(unsigned int tics, bool updateState, bool renderOnly);

        double makeAction(std::vector<int> const &actions);
        double makeAction(std::vector<int> const &actions, unsigned int tics);
        
        State getState();

        std::vector<int> getLastAction();

        bool isNewEpisode();
        bool isEpisodeFinished();

        bool isPlayerDead();
        void respawnPlayer();

        void addAvailableButton(Button button);
        void addAvailableButton(Button button, int maxValue);
        void clearAvailableButtons();
        int getAvailableButtonsSize();
        void setButtonMaxValue(Button button, int maxValue);
        int getButtonMaxValue(Button button);

        void addAvailableGameVariable(GameVariable var);

        void clearAvailableGameVariables();
        int getAvailableGameVariablesSize();

        void addGameArgs(std::string args);
        void clearGameArgs();

        void sendGameCommand(std::string cmd);

        uint8_t * const getGameScreen();

        Mode getMode();
        void setMode(Mode mode);

        //OPTIONS

        int getGameVariable(GameVariable var);

        double getLivingReward();
        void setLivingReward(double livingReward);
        double getDeathPenalty();
        void setDeathPenalty(double deathPenalty);

        double getLastReward();
        double getSummaryReward();

        void setDoomEnginePath(std::string path);
        void setDoomGamePath(std::string path);
        void setDoomScenarioPath(std::string path);
        void setDoomMap(std::string map);
        void setDoomSkill(int skill);
        void setDoomConfigPath(std::string path);

        unsigned int getSeed();
        void setSeed(unsigned int seed);

        unsigned int getEpisodeStartTime();
        void setEpisodeStartTime(unsigned int tics);

        unsigned int getEpisodeTimeout();
        void setEpisodeTimeout(unsigned int tics);

        unsigned int getEpisodeTime();

        void setScreenResolution(ScreenResolution resolution);
        void setScreenFormat(ScreenFormat format);
        void setRenderHud(bool hud);
        void setRenderWeapon(bool weapon);
        void setRenderCrosshair(bool crosshair);
        void setRenderDecals(bool decals);
        void setRenderParticles(bool particles);
        void setWindowVisible(bool visibility);
        void setConsoleEnabled(bool console);

        int getScreenWidth();
        int getScreenHeight();
        int getScreenChannels();
        size_t getScreenPitch();
        size_t getScreenSize();

        ScreenFormat getScreenFormat();

    protected:

        DoomController *doomController;
        bool running;

        /* STATE AND ACTIONS */
        Mode mode;

        State state;
        void updateState();

        std::vector <GameVariable> availableGameVariables;
        std::vector <Button> availableButtons;

        std::vector<int> lastAction;

        /* Reward */
        unsigned int nextStateNumber;
        unsigned int lastMapTic;

        double lastReward;
        double lastMapReward;
        double summaryReward;

        double livingReward;
        double deathPenalty;

    private:
        /* Load config helpers */
        static bool StringToBool(std::string boolString);
        static ScreenResolution StringToResolution(std::string str);
        static ScreenFormat StringToFormat(std::string str);
        static Button StringToButton(std::string str);
        static GameVariable StringToGameVariable(std::string str);
        static unsigned int StringToUint(std::string str);
        static bool ParseListProperty(int &line_number, std::string &value, std::ifstream& input, std::vector<std::string> &output);

    };
}

#endif
