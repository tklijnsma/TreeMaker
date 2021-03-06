import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/02693A18-FAE9-E811-B1E2-3417EBE65F56.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0EC24D9A-0EEA-E811-AFEB-3417EBE6451F.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/1078DC26-1DEA-E811-9B78-3417EBE2F478.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/18FBF199-0EEA-E811-B7AF-008CFAFBFC72.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/2004D49B-0AEA-E811-818F-008CFAF73658.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/203CE578-20EA-E811-87EA-7CD30AD08F62.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/20440836-0BEA-E811-9C37-008CFAFBE880.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/20EDC1B5-23EA-E811-93C3-7CD30ACDD21A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/2426BB0B-5BEA-E811-86FB-3417EBE64BA3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/28366500-E5E9-E811-AAF2-008CFAF35AC0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/2CD68180-12EA-E811-9DB8-7CD30AB15C58.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/2E645DD5-3DEA-E811-9E57-509A4C748A49.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/32837197-12EA-E811-9770-3417EBE338FA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3684B373-12EA-E811-AF36-509A4C78137D.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3A7F5FD9-06EA-E811-8738-7CD30AD09D1E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3CCCE6C8-09EA-E811-95CF-7845C4FB6238.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/44647D14-5AEA-E811-BCD3-008CFAF35AC0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4A65BA06-0BEA-E811-83F7-008CFAFBFCA8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/4CB06953-85EA-E811-8731-509A4C781325.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/52AD78CB-0AEA-E811-A526-3417EBE2EC95.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/5E7F6D9B-12EA-E811-BBD4-7CD30AD0A168.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/640E9913-16EA-E811-BA3D-509A4C7812F3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/70E09B14-0CEA-E811-9707-7CD30AB049DA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/88E9E192-12EA-E811-9165-509A4C8605EA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/94DB92A0-05EA-E811-B701-008CFAF72404.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/94ED4BC3-12EA-E811-B3D5-7845C4F9795F.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A4AF0A63-05EA-E811-A65E-509A4C730E30.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A837092B-12EA-E811-947B-509A4C858B2B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/C84F537E-E7E9-E811-9109-509A4C748A68.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/C8BC1736-12EA-E811-979A-3417EBE65F56.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D4F2FED9-21EA-E811-815B-509A4C74908E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D6805BE2-09EA-E811-811A-509A4C748AAD.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D877CA75-F5E9-E811-BB7A-F04DA275C316.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DA0731FF-09EA-E811-A648-7CD30AD08CFE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DA9FFDD7-08EA-E811-8979-7CD30AD09004.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DCEADCAB-2BEA-E811-938D-509A4C748A49.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DCF567F5-05EA-E811-997D-7CD30AD09C64.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E6027A63-0FEA-E811-A1AE-3417EBE2EE2D.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E862339A-08EA-E811-B9BA-509A4C748037.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F08A1FD7-FAE9-E811-8401-7CD30AD09C10.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/346128D8-EFE9-E811-890D-7CD30AD09D1E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/460F757C-EEE9-E811-A2FB-7CD30ACDCF08.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/780999F2-EBE9-E811-9694-3417EBE644B3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/AA12152D-4FEA-E811-BD7F-3417EBE64567.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D8B03507-F2E9-E811-84E1-7CD30ACDE0CC.root',
] )
